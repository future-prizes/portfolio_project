const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");




async function login(event) {
    event.preventDefault()
    const loginFormData = new FormData(loginForm)

    if (!loginForm.checkValidity()){
        loginForm.checkValidity();
        return
    }
    try {
        const result = await fetch(url, {
        method:"POST",
        body: loginFormData
    })
    if (!result.ok){
        throw new Error("no response")
    }
    const response = result.json()
    }

    catch (error){
        return error.message
    }};

async function register(event) {
    event.preventDefault()
    const registerFormData = new FormData(registerForm)

    if (!registerForm.checkValidity()){
        registerForm.checkValidity();
        return
    }
    try {
        const result = await fetch(url, {
            method: "POST",
            body: registerFormData
        })
        if (!result.ok) {
            throw new Error("no response")
        }

    }
    catch (error) {
        return error.message
    }
}