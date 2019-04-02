module.exports = {
  devServer: {
    proxy: 'http://localhost:5000/',
    /*
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to flask dev server
        target: 'http://backend:5000/'
      }
    }*/
  },
}
