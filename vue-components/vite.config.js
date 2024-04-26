export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame_tweakpane",
      formats: ["umd"],
      fileName: "trame_tweakpane",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../trame_tweakpane/module/serve",
    assetsDir: ".",
  },
};
