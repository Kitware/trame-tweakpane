import components from "./components";

export function install(Vue) {
  Object.keys(components).forEach((name) => {
    Vue.component(`tp-${name.toLowerCase()}`, components[name]);
  });
}
