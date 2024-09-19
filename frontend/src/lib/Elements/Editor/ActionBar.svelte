<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import {
    VscChevronLeft,
    VscChevronRight,
    VscEdit,
    VscSave,
    VscChromeClose,
  } from "svelte-icons-pack/vsc";
  import {
    explorerVisible,
    fileSelected,
    dataToUpdate,
    isLogged
  } from "../../../stores/store";
  import { closeFile, sendUpdate, toogleModeEditor } from "./functions";

  function toggleExplorerVisible() {
    explorerVisible.update((state) => !state);
  }

  function saveFile() {
    if ($dataToUpdate != null) {
      sendUpdate();
      toogleModeEditor();
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
    {/if}
    <button
      on:click={closeFile}
      class=" ml-auto rounded-full hover:bg-zinc-800 hover:text-neutral-300 p-1"
    >
      <Icon src={VscChromeClose} size={22} />
    </button>
  {/if}
</div>
