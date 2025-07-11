<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import {
    VscChevronLeft,
    VscChevronRight,
    VscEdit,
    VscSave,
    VscChromeClose,
    VscDesktopDownload
  } from "svelte-icons-pack/vsc";
  import { BsFileEarmarkArrowDown, BsFileEarmarkArrowUp } from "svelte-icons-pack/bs";
  import {
    explorerVisible,
    fileSelected,
    dataToUpdate,
    isLogged,

    backupProjectToUpload,

    templateEditor


  } from "../../../stores/store";
  import { closeFile, sendUpdate, download_file, toogleModeEditor } from "./functions";
  import { get } from "svelte/store";
  import type { ContentBlankInterface, ContentProjectInterface } from "../../Components/Interfaces/ContentFileInterface";

  //HTML Elements
  let inputBackup: HTMLInputElement | undefined;

  function toggleExplorerVisible() {
    explorerVisible.update((state) => !state);
  }

  function saveFile() {
    if ($dataToUpdate !== null) {
      sendUpdate();
      toogleModeEditor();
    }
  }
  
  function clickInputBackukp(e: Event) {
    if (!inputBackup) { return };
    inputBackup.click();
  }
  
  function onBackupSelected(e: Event) {
    const target = e.target as HTMLInputElement;
    console.log(target.files?.length)
    if (target && target.files?.length) {
      backupProjectToUpload.set(target.files[0]);
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
      sendUpdate();
      target.value = ""; // Limpiando el input
    }
  }
  
</script>

<div
  class="flex flex-row gap-3 bg-transparent border-b border-zinc-800 p-1 min-h-10"
>
  <button
    class="rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
    on:click={toggleExplorerVisible}
  >
    <Icon src={$explorerVisible ? VscChevronLeft : VscChevronRight} size={22} />
  </button>
  {#if $fileSelected.id != ""}
    {#if $isLogged}
      <div class="flex flex-row gap-8">
        <div class="flex flex-row gap-2">
          <button
            on:click={saveFile}
            class=" rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
          >
            <Icon src={VscSave} size={22} />
          </button>
          <button
            on:click={toogleModeEditor}
            class=" rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
          >
            <Icon src={VscEdit} size={22} />
          </button>
        </div>
        <div class="flex flex-row gap-2">  
          <button
            on:click={download_file}
            class=" rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
          >
            <Icon src={BsFileEarmarkArrowDown} size={22} />
          </button>
          <button
            on:click={(e) => clickInputBackukp(e)}
            class=" rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
          >
            <Icon src={BsFileEarmarkArrowUp} size={22} />
            <div class="hidden">
              <input bind:this={inputBackup} name="backup_project" 
              class="w-fit rounded p-1 hover:cursor-pointer bg-zinc-800 outline-none" 
              type="file" 
              accept=".zip" 
              on:input={e=>onBackupSelected(e)}
              >
            </div>
          </button>
        </div>
      </div>
    {/if}
    <button
      on:click={closeFile}
      class=" ml-auto rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
    >
      <Icon src={VscChromeClose} size={22} />
    </button>
  {/if}
</div>
