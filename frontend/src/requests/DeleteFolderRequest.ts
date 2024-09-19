import { get } from "svelte/store";
import { closeFile } from "../lib/Elements/Editor/functions";
import { response_401 } from "../responses/error";
import { getMainData } from "./MainDataRequest";
import { URLServer } from "../stores/store";

export default async function deleteFolderRequest (id: string) {
    try {
      const res = await fetch(`${get(URLServer)}/api/delete/folder`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify({
          id: id
        })
      });
      await getMainData();
      closeFile();
    } catch (error) {
      response_401()
    }
}