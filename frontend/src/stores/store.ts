import { readable, writable, type Writable } from "svelte/store";
import type { DataElementType } from "../lib/Components/types/DataElementType";
import type { FileInterface } from "../lib/Components/Interfaces/FileInterface";
import { persistent } from "./localStorage";

export const modeEditor = writable("read");
export const templateEditor = writable("init");
export const contentEditor: Writable<string> | any = writable("");
export const dataToUpdate = writable<FileInterface|null>(null);
export const imagesToUpload = writable<FileList|null>(null);
export const imagesToDelete = writable<string[]>([]); 

export const fileSelected = writable<{id:string, name:string}>({id:"", name:""});
export const imgModal = writable("");

export const mainData = writable<DataElementType[]>();

export const modalVisible = writable(false);
export const explorerVisible = writable(true);

export const loginVisible = writable(false);
export const isLogged = writable(false);
localStorage.getItem("username") ? isLogged.set(true) : isLogged.set(false);

export const usernameSession = persistent("username","");

//export const URLServer = readable("https://tournament.com")
export const URLServer = readable(window.location.origin)