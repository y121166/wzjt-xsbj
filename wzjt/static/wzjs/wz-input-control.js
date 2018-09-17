// ----------------------------------------------------------------------
// <summary>
// 限制只能输入数字
// </summary>
// ----------------------------------------------------------------------
$.fn.onlyNum = function () {
    $(this).focus(function () {
        if (this.value === '0.00') {
                this.value = '';
            } else {
                this.value = this.value.replace(/\.00/, '').replace(/(\.\d)0/,'$1');
            }
            precapital = this.value;
    });

    $(this).keyup(function () {
        this.value = this.value.replace(/^[\.]/, '').replace(/[^\d.]/g, '');
        if (this.value.split(".").length - 1 > 1) {
            this.value = precapital;
        }
        precapital = this.value;
    });

    $(this).blur(function () {
        this.value = this.value.replace(/[\.]$/, '');
        this.value = this.value.replace(/(.*)\.([\d]{2})(\d*)/g,'$1.$2');
        this.value = Number(this.value).toFixed(2);
        var logNum = this.value.toString();
        if(logNum.match(/\./g) != null){
            integerNum = parseInt(logNum).toString().replace(/\d(?=(\d{3})+$)/g,'$&,');
            decimalNum = '.' + logNum.replace(/(.*)\.(.*)/g,'$2');
        }else{

        }
    });
};

// ----------------------------------------------------------------------
// <summary>
// 限制只能输入字母
// </summary>
// ----------------------------------------------------------------------
$.fn.onlyAlpha = function () {
    $(this).keypress(function (event) {
        var eventObj = event || e;
        var keyCode = eventObj.keyCode || eventObj.which;
        if ((keyCode >= 65 && keyCode <= 90) || (keyCode >= 97 && keyCode <= 122))
            return true;
        else
            return false;
    }).focus(function () {
        this.style.imeMode = 'disabled';
    }).bind("paste", function () {
        var clipboard = window.clipboardData.getData("Text");
        if (/^[a-zA-Z]+$/.test(clipboard))
            return true;
        else
            return false;
    });
};

// ----------------------------------------------------------------------
// <summary>
// 限制只能输入数字和字母
// </summary>
// ----------------------------------------------------------------------
$.fn.onlyNumAlpha = function () {
    $(this).keypress(function (event) {
        var eventObj = event || e;
        var keyCode = eventObj.keyCode || eventObj.which;
        if ((keyCode >= 48 && keyCode <= 57) || (keyCode >= 65 && keyCode <= 90) || (keyCode >= 97 && keyCode <= 122))
            return true;
        else
            return false;
    }).focus(function () {
        this.style.imeMode = 'disabled';
    }).bind("paste", function () {
        var clipboard = window.clipboardData.getData("Text");
        if (/^(\d|[a-zA-Z])+$/.test(clipboard))
            return true;
        else
            return false;
    });
};

$(function () {
    // 限制使用了onlyNum类样式的控件只能输入数字
    $(".onlyNum").onlyNum();
    //限制使用了onlyAlpha类样式的控件只能输入字母
    $(".onlyAlpha").onlyAlpha();
    // 限制使用了onlyNumAlpha类样式的控件只能输入数字和字母
    $(".onlyNumAlpha").onlyNumAlpha();
   });