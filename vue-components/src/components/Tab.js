const { computed, inject, provide } = window.Vue;

export default {
  props: {
    index: {
      type: Number,
      default: 0,
    },
  },

  setup(props) {
    const tabs = inject("tabs");
    const page = computed(() => {
      if (!tabs.value) {
        return null;
      }
      return tabs.value.pages[props.index];
    });
    provide("pane", page);
  },
  template: "<slot />",
};
