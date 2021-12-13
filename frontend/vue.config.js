module.exports = {
  devServer: {
    proxy: 'http://backend:5000/',
    /*
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to flask dev server
        target: 'http://backend:5000/'
      }
    }*/
    // https://github.com/vuejs/vue-cli/issues/4557
    progress: false,
  },
}
