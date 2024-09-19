<script lang="ts">
  import InputNewFile from "../Elements/Explorer/InputNewFile.svelte";
  import File from "./File.svelte";
  import Folder from "./Folder.svelte";
  import { isFileInterface } from "./Interfaces/FileInterface";
  import type { FileInterface } from "./Interfaces/FileInterface";
  import { isFolderInterface, type FolderInterface } from "./Interfaces/FolderInterface";

  export let dataElement: FileInterface | FolderInterface;
  let viewInput: boolean;
  let openInput: () => void;
  let closeInput: () => void;
  if (isFolderInterface(dataElement)) {
    
    viewInput = false;
    openInput = () => {viewInput = true}
    closeInput = () => {viewInput = false}
  }
</script>

{#if isFileInterface(dataElement)}
  <File id={dataElement.id} nameFile={dataElement.name} template={dataElement.template} fileContent={dataElement.content} />
{:else if isFolderInterface(dataElement)}
  <Folder nameFolder={dataElement.name} id={dataElement.id} openInput={openInput}>
    <InputNewFile folderId={dataElement.id} viewInput={viewInput} closeInput={closeInput}/>
    {#each dataElement.files as file}
      <File
        id={file.id}
        nameFile={file.name}
        template={file.template}
        fileContent={file.content}
      />
    {/each}
  </Folder>
{/if}
