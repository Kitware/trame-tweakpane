const { unref, watch, inject, onBeforeUnmount } = window.Vue;

export default {
  emits: ["change"],
  props: {
    options: {
      type: Object,
      default: () => ({}),
    },
    name: {
      type: String,
      default: null,
    },
  },
  setup(props, { emit }) {
    const key = props.name;
    const pane = inject("pane");
    const trame = inject("trame");
    const param = { [key]: unref(trame.state.get(props.name)) };
    let binding = null;

    function update({ value }) {
      if (value instanceof Object) {
        trame.state.set(props.name, { ...param[key] });
      } else {
        trame.state.set(props.name, param[key]);
      }

      emit("change", value);
    }

    function onDirty({ keys }) {
      if (keys.includes(props.name)) {
        param[key] = trame.state.get(props.name);
        binding.refresh();
      }
    }

    onBeforeUnmount(() => {
      trame.state.removeListener(onDirty);
      binding.off("change", update);
      binding.dispose();
    });
    watch(
      () => pane.value,
      (pane) => {
        if (!pane) return;
        binding = unref(pane).addBinding(param, key, props.options);
        trame.state.addListener(onDirty);
        binding.on("change", update);
      }
    );
  },
};
