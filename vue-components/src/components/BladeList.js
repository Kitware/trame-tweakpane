const { ref, unref, watch, onBeforeUnmount, inject } = window.Vue;
import { fillAddOn } from "../utils/blades";
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
    label: {
      type: String,
    },
    value: {
      type: Number,
      default: "",
    },
    options: {
      type: Array,
      default: () => [],
    },
  },
  emits: ["change"],
  setup(props, { emit }) {
    const pane = inject("pane");
    const blade = ref(null);

    function onUpdate({ value }) {
      emit("change", value);
    }

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
          view: "list",
          hidden: props.hidden,
          disabled: props.disabled,
          ...fillAddOn(props, ["label", "value", "options"]),
        });
        unref(blade).on("change", onUpdate);
      }
    );

    onBeforeUnmount(() => {
      unref(blade).off("change", onUpdate);
      unref(blade).dispose();
    });
  },
};
