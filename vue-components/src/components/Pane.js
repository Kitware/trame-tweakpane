import { Pane } from "tweakpane";

const { ref, unref, onMounted, onBeforeUnmount, provide } = window.Vue;

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
  },
  emits: ["created", "change", "deleted", "export"],
  setup(props, { emit, expose }) {
    const elem = ref(null);
    const pane = ref(null);
    provide("pane", pane);

    function importState(state) {
      unref(pane).importState(state);
    }

    function exportState() {
      emit("export", unref(pane).exportState());
    }

    onMounted(() => {
      const container = unref(elem);
      pane.value = new Pane({
        container,
        expanded: props.expanded,
        title: props.title,
      });
      emit("create", unref(pane));
    });

    onBeforeUnmount(() => {
      unref(pane).dispose();
      emit("deleted");
    });
    expose({ exportState, importState });
    return { elem };
  },
  template: `<div ref="elem"><slot></slot></div>`,
};
