import { getMainData } from "../../../requests/MainDataRequest";
import { response_401 } from "../../../responses/error";
import { fileSelected, templateEditor, dataToUpdate, modeEditor, imagesToUpload, imagesToDelete, URLServer } from "../../../stores/store";
import type { ContentBlankInterface, ContentProjectInterface } from "../../Components/Interfaces/ContentFileInterface";
import { get } from "svelte/store";

export function closeFile() {
    templateEditor.set("init");
    fileSelected.set({ id: "", name: "" });
}

export function toogleModeEditor() {
    imagesToUpload.set(null);
    imagesToDelete.set([]);
    modeEditor.update((mode) => {
      if (mode === "read") {
          let newContent: ContentBlankInterface | ContentProjectInterface = {
              "": "",
            };
            if (get(templateEditor) === "project") {
          newContent = { name: "", description: "" , technologys: [], images: [], url: "", github: ""};
        }
        dataToUpdate.set({
            id: get(fileSelected).id,
            name: "",
            id_folder: "",
            template: "",
            type: "",
          content: newContent,
        });

        return "edit";
      } else {
        dataToUpdate.set(null);

        return "read";
      }
    });
}

export function saveFile() {
    if (get(dataToUpdate) != null) {
      sendUpdate();
      toogleModeEditor();
    }
  }

export  async function sendUpdate() {
    const formData = new FormData();
    const newImages = get(imagesToUpload)
    const deleteImages = get(imagesToDelete)

    if (newImages) {
      Array.from(newImages).forEach(image => {
        formData.append('new_images', image)
      });
    }

    if (deleteImages) {
      formData.append('delete_images', JSON.stringify(deleteImages))
    }

    const data = get(dataToUpdate)
    if (data){
      formData.append('id', data.id)
      formData.append('id_folder', data.id_folder ? data.id_folder : "")
      formData.append('name', data.name)
      formData.append('content', JSON.stringify(data.content))
      formData.append('template', data.template)
      formData.append('type', data.type)
    }

    
    let res: Response;
    try {
    res = await fetch(`${get(URLServer)}/api/update/file`, {
        method: "PATCH",
        credentials: "include",
        body: formData,
    });
    
    if (res.ok) {
        closeFile();
        getMainData();
    }
    } catch (error) {
        response_401();
    }
  }