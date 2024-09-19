<script lang="ts">
  import { fade, slide } from "svelte/transition";
  import { dataToUpdate, modeEditor } from "../../../stores/store";
  import { isContentBlankInterface } from "../Interfaces/ContentFileInterface";
  export let content: { "": string };
  let listP = content[""].split(".");

  function updateDataFile(e: Event) {
    if (
      e.target != null &&
      "value" in e.target &&
      typeof e.target.value === "string"
    ) {
      let value: string = e.target.value;
      dataToUpdate.update((data) => {
        if (isContentBlankInterface(data?.content)) {
          data.content[""] = value;
        }

        return data;
      });
    }
  }
</script>

<div class="flex h-full flex-col gap-3 text-zinc-400 text-lg">
  {#if $modeEditor === "read"}
    <textarea
      disabled
      class="bg-zinc-900 w-full h-full outline-none overflow-y-hidden"
      >{content[""]}</textarea
    >
  {:else if $modeEditor === "edit"}
    <textarea
      on:input={(e) => updateDataFile(e)}
      class="bg-zinc-800 w-full h-full outline-none">{content[""]}</textarea
    >
  {/if}
</div>
