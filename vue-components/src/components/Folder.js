const { ref, unref, watch, onBeforeUnmount, inject, provide } = window.Vue;

export default {
  props: {
    expanded: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      default: "",
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
    const parent = inject("pane");
    const pane = ref(null);
    provide("pane", pane);

    watch(
      () => props.hidden,
      (h) => (pane.value.hidden = h)
    );
    watch(
      () => props.disabled,
      (h) => (pane.value.disabled = h)
    );

    watch(
      () => unref(parent),
      (p) => {
        if (!p) return;
        pane.value = p.addFolder({
          title: props.title,
          expanded: props.expanded,
        });
      }
    );

    onBeforeUnmount(() => {
      unref(pane).dispose();
    });
  },
  template: "<slot />",
};
