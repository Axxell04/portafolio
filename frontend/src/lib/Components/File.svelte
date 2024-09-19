<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import { VscCheck, VscChromeClose, VscFile, VscTrash } from "svelte-icons-pack/vsc";
  import {
    fileSelected,
    contentEditor,
    templateEditor,
    modeEditor,
    dataToUpdate,
    isLogged,
  } from "../../stores/store";
  import { toogleModeEditor } from "../Elements/Editor/functions";
  import type {
    ContentBlankInterface,
    ContentProjectInterface,
  } from "./Interfaces/ContentFileInterface";
  import deleteFileRequest from "../../requests/DeleteFileRequest";

  export let id: string;
  export let nameFile: string;
  export let fileContent: ContentBlankInterface | ContentProjectInterface;
  export let template: string;

  let deletingFile = false;
  $: isSelected = $fileSelected.name === nameFile;
  $: isEditing = isSelected && $modeEditor === "edit";

  const selectFile = () => {
    fileSelected.set({ id: id, name: nameFile });
    contentEditor.set(fileContent);
    templateEditor.update((actualTemplate) => {
      if (actualTemplate === "blank" && template === "blank") {
        return "blank_alt"
      }
      if (actualTemplate === "project" && template === "project") {
        return "project_alt"
      } 
      return template
    })
    $modeEditor === "edit" ? toogleModeEditor() : null;
  };

  function updateNameFile(e: Event) {
    if (
      e.target != null &&
      "value" in e.target &&
      typeof e.target.value === "string"
    ) {
      let value = e.target.value;
      console.log(value);
      dataToUpdate.update((data) => {
        if (data != null && "name" in data) {
          data.name = value;
        }
        return data;
      });
    }
  }

  function toggleDeletingFile () {
    deletingFile = !deletingFile;
  }
  
  function deleteFile () {
    deleteFileRequest(id);
  }

</script>

<div class="flex flex-row">
  <button
    class="{isSelected
      ? 'text-zinc-300'
      : 'text-zinc-400'} px-1 flex flex-row gap-1 place-items-center hover:text-zinc-300 cursor-pointer"
    on:click={isEditing ? null : selectFile}
  >
    <Icon src={VscFile} />
    {#if isEditing}
      <input
        class=" bg-neutral-800 overflow-x-hidden w-32"
        type="text"
        value={nameFile}
        on:input={(e) => updateNameFile(e)}
      />
    {:else}
      <span>{nameFile}</span>
    {/if}
  </button>
  {#if !deletingFile && $isLogged}
  <button class=" ml-auto text-neutral-400 rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300" on:click={toggleDeletingFile}>
    <Icon src={VscTrash}/>
  </button>
  {:else if deletingFile && $isLogged}
  <button class=" ml-auto text-neutral-400 rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300" on:click={deleteFile}>
    <Icon src={VscCheck}/>
  </button>
  <button class=" text-neutral-400 rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300" on:click={toggleDeletingFile}>
    <Icon src={VscChromeClose}/>
  </button>
  {/if}
</div>
