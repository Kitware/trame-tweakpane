const { unref, watch, onBeforeUnmount, inject } = window.Vue;

export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    title: {
      type: String,
      default: "",
    },
  },

  setup(props, { emit }) {
    const pane = inject("pane");
    let button = null;
    function onClick() {
      emit("click");
    }

    watch(
      () => unref(pane),
      (p) => {
        if (!p) return;
        button = p.addButton({
          title: props.title,
          label: props.label,
        });
        button.on("click", onClick);
      }
    );

    onBeforeUnmount(() => {
      button.off("click", onClick);
      unref(pane).dispose();
    });
  },
};
