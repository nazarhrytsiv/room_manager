function validate_input_string(obj) {
    var input_text = obj["value"];
    if (!input_text.length)
    {
        $(obj).addClass("invalid").removeClass("valid");
        $(obj).next().removeClass("invisible").text("Cannot be empty");
        return false;
    }
    $(obj).addClass("valid").removeClass("invalid");
    $(obj).next().addClass("invisible");
    return true;
}

function validate_input_integer(obj) {
    var input_text = obj["value"];
    if (isNaN(input_text))
    {
        $(obj).addClass("invalid").removeClass("valid");
        $(obj).next().removeClass("invisible").text("Must be integer.");
        return false;
    }
    if (Number(input_text) <= 0)
    {
        $(obj).addClass("invalid").removeClass("valid");
        $(obj).next().removeClass("invisible").text("Cannot be less than zero.");
        return false;
    }
    $(obj).addClass("valid").removeClass("invalid");
    $(obj).next().addClass("invisible");
    return true;
}
