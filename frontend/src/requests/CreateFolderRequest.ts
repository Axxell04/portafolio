import { get } from "svelte/store";
import { closeFile } from "../lib/Elements/Editor/functions";
import { response_401 } from "../responses/error";
import { URLServer } from "../stores/store";
import { getMainData } from "./MainDataRequest";


export default async function createFolderRequest (nameNewFolder: string) {
    try {
        const res = await fetch(`${get(URLServer)}/api/create/folder`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify({
            name: nameNewFolder
        })
        });
        await getMainData();
        closeFile();
    } catch (error) {
        response_401()
    }
}