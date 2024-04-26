export function fillAddOn(props, names) {
  const addon = {};
  for (let i = 0; i < names.length; i++) {
    const name = names[i];
    if (props[name] !== undefined) {
      addon[name] = props[name];
    }
  }
  return addon;
}
