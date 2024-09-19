<script lang="ts">
  import Explorer from './lib/Elements/Explorer/Explorer.svelte';
  import Editor from './lib/Elements/Editor/Editor.svelte';
  import Modal from './lib/Elements/Modal/Modal.svelte';
  import { explorerVisible } from './stores/store';
  import { slide } from 'svelte/transition';
</script>

<main class="bg-zinc-900 min-h-dvh flex flex-row">
  {#if $explorerVisible}
  <div transition:slide={{axis: "x", duration: 600}}>
    <Explorer />
  </div>    
  {/if}
  <Editor />
  <Modal />
</main>
