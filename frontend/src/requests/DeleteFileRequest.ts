import { get } from "svelte/store";
import { closeFile } from "../lib/Elements/Editor/functions";
import { getMainData } from "./MainDataRequest";
import { URLServer } from "../stores/store";

export default async function deleteFileRequest(id: string) {
    const res = await fetch(`${get(URLServer)}/api/delete/file`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ id: id }),
    });
    getMainData();
    closeFile();
}