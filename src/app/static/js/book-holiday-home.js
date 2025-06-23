$(document).ready(function () {

    $("#languages").change(function () {
        fetch(window.location.href, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `lang=${$(this).val()}`,
        })
            .then(response => {
                if (response.status === 200) {
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error(error);
            });
    });

    $("#name").click(function () {
        window.location.href = "/"
    });

    fetch("/disable_days", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then((response) => response.json())
        .then((dates) => {

            disableDays = []
            disableDays.push(...dates);
            flatpickr("#days", {
                mode: "range",
                minDate: "today",
                disable: disableDays,
                locale: $("#locale").val(),
                dateFormat: $("#dateFormat").val()
            });

        })
        .catch((error) => {
            console.error(error);
        });

    $("#calender").click(function () {
        $("#days").click();
    });

    $("form").on("submit", function () {
        $("#book").prop("disabled", true);
    });

    $(document).on("keypress", function (e) {
        if (e.which == 13) {
            $("#book").click();
        }
    });

});