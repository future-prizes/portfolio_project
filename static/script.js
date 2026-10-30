const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const button = document.querySelector("button");
const h2 = document.querySelector("h2");
const hostURL = "http://127.0.0.1"
const port = "5000"




async function login(event) {
    event.preventDefault()
    const loginFormData = new FormData(loginForm)
    const loginURL = new URL("/login", `${hostURL}:${port}`)

    if (!loginForm.checkValidity()){
        loginForm.checkValidity();
        return
    }
    try {
        const result = await fetch(loginURL, {
        method:"POST",
        body: loginFormData
    })
    if (!result.ok){
        throw new Error("no response")
    }
    const response = await result.json()
    }

    catch (error){
        return error.message
    }
    loginForm.reset()
    };

async function register(event) {
    event.preventDefault()
    const registerFormData = new FormData(registerForm)
    const regiserURL = new URL("/register", `${hostURL}:${port}`)

    if (!registerForm.checkValidity()){
        registerForm.checkValidity();
        return
    }
    try {
        const result = await fetch(regiserURL, {
            method: "POST",
            body: registerFormData
        })
        if (!result.ok) {
            throw new Error("no response")
        }
        const response = await result.json()
        h2.textContent = response

    }
    catch (error) {
        return error.message
    }
    registerForm.reset()
    }

async function showAll(){
    const fetchAllURL = new URL("/show-all", `${hostURL}:${port}`)
    try {
        const result = await fetch(fetchAllURL, {
            method: "GET"
        })
        if (!result.ok) {
            throw new Error("no response")
        }
        const response = await result.json()
        h2.textContent = response
    }
    catch (error) {
        return error.message
    }
}
console.log(document.getElementById("loginForm"))
loginForm?.addEventListener("submit", (event) => {login(event)})
registerForm?.addEventListener("submit", (event) =>{register(event)})