let socket = new WebSocket("ws://localhost:8000/ws/test/"); // TODO make url generic

socket.onopen = function () {
    console.log("Connected");

    socket.send("Send data as string");

    setTimeout(() => {
        socket.send(JSON.stringify(
            {
                value: 42,
                label: 'Magic number'
            }
        ));

    }, 2000);
};

socket.onclose = function (event) {
    if (event.wasClean) {
        console.log('Connection has been closed correctly');
    } else {
        console.log('Disconnected');
    }
    console.log('Status code: ' + event.code + ' reason: ' + event.reason);
};

socket.onmessage = function (event) {
    console.log("Received data " + event.data);
};

socket.onerror = function (error) {
    console.log("Error " + error.message);
};

let chatInput = document.getElementById('say_to_bot');
let submitButton = document.getElementById('send_button');
let chatForm = document.getElementById('chat_form');

let sendHandler = function (event) {
    console.log('DEBUG Submitted');
    let data = {
        value: chatInput.value.trim()
    };
    if (data.value) {
        socket.send(JSON.stringify(data))
    } else {
        chatInput.value = '';
    }

    event.preventDefault(); // disable submitting form
};

chatForm.addEventListener("submit", sendHandler);
submitButton.addEventListener("click", sendHandler);
