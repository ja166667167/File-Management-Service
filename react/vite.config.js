import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [react()],
//   build: {
//     outDir: "build",
//   },
//   server: {
//     watch: {
//       usePolling: true,
//     },
//     host: true, // needed for the Docker Container port mapping to work
//     strictPort: true,
//     port: import.meta.env.VITE_REACT_PORT,
//     // port: 81,
//   },
// });
export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd());
  return defineConfig({
    plugins: [react()],
    build: {
      outDir: "build",
    },
    server: {
      watch: {
        usePolling: true,
      },
      host: true, // needed for the Docker Container port mapping to work
      strictPort: true,
      port: env.VITE_REACT_PORT,
      // port: 81,
    },
  });
};
