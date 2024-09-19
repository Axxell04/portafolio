import { isLogged, usernameSession } from "../stores/store";

export function response_401 () {
    usernameSession.set("");
    isLogged.set(false);
}