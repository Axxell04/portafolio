<script lang="ts">
  import { fade, fly, slide } from "svelte/transition";
  import { templateEditor, contentEditor, fileSelected } from "../../../stores/store";
  import Blank from "../../Components/templates/Blank.svelte";
  import Project from "../../Components/templates/Project.svelte";
  import ActionBar from "./ActionBar.svelte";

  let visible: boolean = true;
  templateEditor.subscribe((value) => {
    console.log(value)
  })
</script>

{#if visible}
  <div
    class="flex flex-col flex-1 outline outline-1 outline-zinc-800 text-neutral-400 h-dvh overflow-y-auto"
  >
    <ActionBar />
    <div class="flex flex-col p-3 overflow-y-auto flex-1">
      {#if $templateEditor === "init"}
        <div transition:slide class="h-full text-4xl font-extralight">
          <p>Hola, soy <span class="font-normal">Axel Lajones</span></p>
          <p>Desarrollador FullStack</p>
          <p>Bienvenido a mi portafolio :)</p>
        </div>
      {:else if $templateEditor === "blank"}
        <div transition:slide class="h-full">
          <svelte:component this={Blank} content={$contentEditor} />
        </div>
      {:else if $templateEditor === "blank_alt"}
        <div transition:slide class="h-full">
          <svelte:component this={Blank} content={$contentEditor} />
        </div>
      {:else if $templateEditor === "project"}
        <div transition:slide>
          <svelte:component this={Project} content={$contentEditor} nameFile={$fileSelected.name}/>
        </div>
      {:else if $templateEditor === "project_alt"}
        <div transition:slide>
          <svelte:component this={Project} content={$contentEditor} nameFile={$fileSelected.name}/>
        </div>
      {/if}
    </div>
  </div>
{/if}
