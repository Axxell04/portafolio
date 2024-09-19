<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import { VscCheck, VscChromeClose } from "svelte-icons-pack/vsc";
  import createFileRequest from "../../../requests/CreateFileRequest";

  export let folderId: string;
  export let viewInput: boolean = true;
  export let closeInput: () => void;
  let nameFile = "";
  let templateSelected = "";

  function selectTemplate (e: Event) {
    if (e.target != null && "textContent" in e.target && typeof e.target.textContent === "string") {
      templateSelected = e.target.textContent;
    }
  }

  function updateName (e: Event) {
    if (e.target != null && "value" in e.target && typeof e.target.value === "string") {
      nameFile = e.target.value;
    }
  }

  function createFile () {
    if (!nameFile || !templateSelected) {return}
    createFileRequest(nameFile, folderId, templateSelected);
    nameFile = "";
    templateSelected = "";
    closeInput();
  }

</script>

{#if viewInput}
<div class="text-neutral-400 flex flex-col">
  <div class="flex flex-row gap-1">
    <input
      type="text"
      class=" bg-neutral-800 text-neutral-300"
      on:input={(e) => updateName(e)}
    />
    <button
      class=" ml-auto rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300"
      on:click={createFile}
    >
      <Icon src={VscCheck} size={20} />
    </button>
    <button
      class=" rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300"
      on:click={closeInput}
    >
      <Icon src={VscChromeClose} size={20} />
    </button>
  </div>
  <div class="flex flex-row gap-2">
    <span>Template: </span>
    <div class="flex flex-row gap-2">
      <button class="px-1 hover:text-neutral-300 hover:border-b {templateSelected === 'Blank' ? 'border-b' : ''}" on:click={e => selectTemplate(e)}>Blank</button>
      <button class="px-1 hover:text-neutral-300 hover:border-b {templateSelected === 'Project' ? 'border-b' : ''}" on:click={e => selectTemplate(e)}>Project</button>
    </div>
  </div>
</div>
{/if}
