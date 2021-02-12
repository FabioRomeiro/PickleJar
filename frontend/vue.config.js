const path = require("path");

const _apimock = process.env.API_MOCK == "1" || (process.env.API_MOCK == undefined && process.env.npm_lifecycle_event == "dev")
const _apijs = _apimock ? "apimock.js" : "api.js";
const pathToApi = path.resolve(__dirname, './src/services/' + _apijs);
console.log(pathToApi);

module.exports = {
    runtimeCompiler: true,
    css: {
        loaderOptions: {
            sass: {
                prependData: `
                    @import "@/assets/scss/_reset.scss";
                    @import "@/assets/scss/_variables.scss";
                    @import "@/assets/scss/_functions.scss";
                    @import "@/assets/scss/_fonts.scss";
                    @import "@/assets/scss/_icons.scss";
                `
            }
        }
    },
    chainWebpack: config => {
        config.resolve.alias
            .set('apijs', pathToApi);
    }
};