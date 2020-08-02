function changeAgeRequest() {
    var newAge = document.getElementById("age_field").value;
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
        var notice = "";
        if (xhr.status >= 200 && xhr.status < 300) {
            var ageField = document.getElementById("age");
            ageField.innerHTML = newAge;
        } else {
            notice += "Error:  ";
        }
        notice += JSON.parse(xhr.responseText)['status'];
        var noticeField = document.getElementById("notice");
        noticeField.innerText = notice;
    };
    var jsonData = {age: newAge};
    var formattedJsonData = JSON.stringify(jsonData);
    xhr.open('POST', '/update_age');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(formattedJsonData)
}