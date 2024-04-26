const { ref, unref, watch, onBeforeUnmount, inject, provide } = window.Vue;

export default {
  props: {
    pages: {
      type: Array,
      default: () => [],
    },
    hidden: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },

  setup(props) {
    const pane = inject("pane");
    const tabs = ref(null);
    provide("tabs", tabs);

    watch(
      () => props.hidden,
      (h) => tabs.value && (tabs.value.hidden = h)
    );
    watch(
      () => props.disabled,
      (h) => tabs.value && (tabs.value.disabled = h)
    );

    watch(
      () => unref(pane),
      (p) => {
        if (!p) return;
        tabs.value = p.addTab({
          hidden: props.hidden,
          disabled: props.disabled,
          pages: props.pages.map((title) => ({ title })),
        });
      }
    );

    onBeforeUnmount(() => {
      unref(tabs).dispose();
    });
  },
  template: "<slot />",
};
