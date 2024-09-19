import { get } from "svelte/store";
import { closeFile } from "../lib/Elements/Editor/functions";
import { response_401 } from "../responses/error";
import { getMainData } from "./MainDataRequest";
import { URLServer } from "../stores/store";

export default async function createFileRequest (nameNewElement: string, id_folder: string = "", template: string) {
    try {
      const res = await fetch(`${get(URLServer)}/api/create/file`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify({
          name: nameNewElement,
          id_folder: id_folder,
          template: template.toLowerCase()
        })
      });
      await getMainData();
      closeFile();
    } catch (error) {
      response_401()
    }
  }