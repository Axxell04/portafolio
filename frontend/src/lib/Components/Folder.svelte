<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import { BsFolder2 } from "svelte-icons-pack/bs";
  import { BsFolder2Open } from "svelte-icons-pack/bs";
  import Content from "./Content.svelte";
  import { VscCheck, VscChromeClose, VscNewFile, VscTrash } from "svelte-icons-pack/vsc";
  import { isLogged } from "../../stores/store";
  import deleteFolderRequest from "../../requests/DeleteFolderRequest";

  //PARAMS
  export let nameFolder: string;
  export let id: string;
  export let openInput: () => void;

  let open: boolean = false;
  let deletingFile = false;

  const toggleOpen = () => {
    open = !open;
  };

  function toggleDeletingFolder () {
    deletingFile = !deletingFile;
  }

  function deleteFolder () {
    deleteFolderRequest(id)
  }

</script>

<div class="flex flex-row">
  <button
    class="text-zinc-400 pl-1 flex flex-row gap-1 place-items-center hover:text-zinc-300 cursor-pointer"
    on:click={toggleOpen}
  >
    <Icon src={open ? BsFolder2Open : BsFolder2} />
    <span>{nameFolder}</span>
  </button>
  {#if !deletingFile && $isLogged}
  <div class="ml-auto">
    <button class="h-fit p-1 self-end rounded-full hover:bg-neutral-800 text-zinc-400 hover:text-zinc-300 " on:click={openInput}>
      <Icon src={VscNewFile}/>
    </button>
    <button class="h-fit p-1 self-end rounded-full hover:bg-neutral-800 text-zinc-400 hover:text-zinc-300 " on:click={toggleDeletingFolder}>
      <Icon src={VscTrash}/>
    </button>
  </div>
  {:else if deletingFile && $isLogged}
  <div class="ml-auto">
    <button class="h-fit p-1 self-end rounded-full hover:bg-neutral-800 text-zinc-400 hover:text-zinc-300 " on:click={deleteFolder}>
      <Icon src={VscCheck}/>
    </button>
    <button class="h-fit p-1 self-end rounded-full hover:bg-neutral-800 text-zinc-400 hover:text-zinc-300 " on:click={toggleDeletingFolder}>
      <Icon src={VscChromeClose}/>
    </button>
  </div>
  {/if}
</div>

<!-- FILES OF FOLDER -->
<Content visible={open}>
  <slot></slot>
</Content>
