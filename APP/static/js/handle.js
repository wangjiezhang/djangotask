$(document).ready(function() {
    $("#sum").click(function() {
        var ip = $("#ip").val();

        $.get("/handle/", {
            'ip': ip
        }, function(ret) {
            $('#result').html(ret)
            get_ips();
        });
    });

    function get_ips() {
        $.get("/ips/", null, function(ret) {
            $('#ips').html(ret)
        })
    }

    var timer;
    document.querySelector('#ip').oninput = function() {
        if (timer) {
            clearTimeout(timer);
        }
        timer = setTimeout(function() {
            $("#sum").click();
        }, 700);
    };
    get_ips(); //页面初次加载时运行
});
