import { writable } from "svelte/store";

export function persistent (key:string, value:string) {
    const storedValue = localStorage.getItem(key);
    const data = storedValue ? storedValue : value;

    const store = writable(data);

    store.subscribe(value => localStorage.setItem(key, value));

    return store;
}