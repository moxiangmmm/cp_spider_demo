/**
 * Created by lenovo on 2018-03-18.
 */
 var createGuid = function () {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    };
var guid = function() {
    return(createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid())
};

