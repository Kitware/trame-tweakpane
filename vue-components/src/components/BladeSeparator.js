const { ref, unref, watch, onBeforeUnmount, inject } = window.Vue;

export default {
  props: {
    hidden: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["change"],
  setup(props) {
    const pane = inject("pane");
    const blade = ref(null);

    watch(
      () => props.hidden,
      (h) => blade.value && (blade.value.hidden = h)
    );
    watch(
      () => props.disabled,
      (h) => blade.value && (blade.value.disabled = h)
    );

    watch(
      () => unref(pane),
      (p) => {
        if (!p) return;
        blade.value = p.addBlade({
          view: "separator",
          hidden: props.hidden,
          disabled: props.disabled,
        });
      }
    );

    onBeforeUnmount(() => {
      unref(blade).dispose();
    });
  },
};
