import { getMainData } from "../../../requests/MainDataRequest";
import { response_401 } from "../../../responses/error";
import {
  fileSelected,
  templateEditor,
  dataToUpdate,
  modeEditor,
  imagesToUpload,
  imagesToDelete,
  backupImagesToUpload,
  URLServer,
  backupProjectToUpload,
} from "../../../stores/store";
import type {
  ContentBlankInterface,
  ContentProjectInterface,
} from "../../Components/Interfaces/ContentFileInterface";
import { get } from "svelte/store";

export function closeFile() {
  templateEditor.set("init");
  fileSelected.set({ id: "", name: "" });
}

export function toogleModeEditor() {
  imagesToUpload.set(null);
  imagesToDelete.set([]);
  backupImagesToUpload.set(null);
  backupProjectToUpload.set(null);
  modeEditor.update((mode) => {
    if (mode === "read") {
      let newContent: ContentBlankInterface | ContentProjectInterface = {
        "": "",
      };
      if (get(templateEditor) === "project") {
        newContent = {
          name: "",
          description: "",
          technologys: [],
          images: [],
          url: "",
          github: "",
        };
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

export async function download_file() {
  if (get(fileSelected).id) {
    try {
      // const res = await fetch(`${get(URLServer)}/api/backup/file/${get(fileSelected).id}`)
      window.location.href = `${get(URLServer)}/api/backup/file/${get(fileSelected).id}`
    } catch (e) {
      response_401()
    }
  }
}

export async function sendUpdate() {
  console.log("Send update")
  const formData = new FormData();
  const newImages = get(imagesToUpload);
  const deleteImages = get(imagesToDelete);
  const backupImages = get(backupImagesToUpload);
  const backupProject = get(backupProjectToUpload);

  if (newImages) {
    Array.from(newImages).forEach((image) => {
      formData.append("new_images", image);
    });
  }

  if (deleteImages) {
    formData.append("delete_images", JSON.stringify(deleteImages));
  }

  if (backupImages) {
    formData.append("backup_images", backupImages);
  }

  if (backupProject) {
    formData.append("backup_project", backupProject)
  }

  const data = get(dataToUpdate);
  if (data) {
    formData.append("id", data.id);
    formData.append("id_folder", data.id_folder ? data.id_folder : "");
    formData.append("name", data.name);
    formData.append("content", JSON.stringify(data.content));
    formData.append("template", data.template);
    formData.append("type", data.type);
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
