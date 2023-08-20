async function OnSubmit() {
    const postData = {
        text: document.querySelector('#text').value
    }

    const parameter = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    }

    const result = await fetch('/add', parameter).then((res) => {
        alert("Registerd.")
        location.reload();
        return res;
    });

}
