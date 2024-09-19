<script lang="ts">
  import { slide } from "svelte/transition";
  import { Icon } from "svelte-icons-pack";
  import { VscAccount, VscAdd, VscCheck, VscChromeClose, VscNewFile, VscNewFolder } from "svelte-icons-pack/vsc";
  import ExpElement from "../../Components/ExpElement.svelte";
  import {
    isLogged,
    loginVisible,
    mainData,
    usernameSession,
  } from "../../../stores/store";

  import { getMainData } from "../../../requests/MainDataRequest";
  import FormLogin from "./FormLogin.svelte";
  import Logout from "./Logout.svelte";
  import createFileRequest from "../../../requests/CreateFileRequest";
  import createFolderRequest from "../../../requests/CreateFolderRequest";
  import { BsGithub } from "svelte-icons-pack/bs";
  import { BiLogoLinkedin } from "svelte-icons-pack/bi";
  import { SiGmail } from "svelte-icons-pack/si";
  import ContactCard from "./ContactCard.svelte";
  import FormContact from "./FormContact.svelte";

  let contactVisible = true;
  let contactFormVisible = false;
  

  const toggleLogin = () => {
    if (contactVisible) {contactVisible = !contactVisible}
    loginVisible.update((value) => !value);
  };

  const toogleContact = () => {
    if ($loginVisible) {loginVisible.set(false)}
    contactVisible = !contactVisible;
  }

  const toogleContactForm = () => {
    contactFormVisible = !contactFormVisible;
  }

  getMainData();

  let creatingElement = false;
  let creatingType = "";
  let nameNewElement = "";
  let templateSelected = "";

  function selectTemplate (e: Event) {
    if (e.target != null && "textContent" in e.target && typeof e.target.textContent === "string") {
      templateSelected = e.target.textContent;
    }
  }

  function openInputNewElement (type: string) {
    creatingElement = true;
    creatingType = type;
  }
  function closeInputNewElement () {
    creatingElement = false;
    creatingType = "";
  }
  function updateNameNewElement (e: Event) {
    if (e.target != null && "value" in e.target && typeof e.target.value === "string") {
      nameNewElement = e.target.value;
    }
  }

  async function createNewFile () {
    if (!nameNewElement || !templateSelected) {return};
    createFileRequest(nameNewElement, "", templateSelected);
    templateSelected = "";
    creatingElement = false;
    nameNewElement = "";
  }

  async function createNewFolder () {
    if (!nameNewElement) {return};
    createFolderRequest(nameNewElement);
    creatingElement = false;
    nameNewElement = "";
  }

  async function createNewElement () {
    if (creatingType === "file") {
      createNewFile();
    } else if (creatingType === "folder") {
      createNewFolder();
    }
  }

</script>

<div
  class=" w-fit min-w-48 bg-neutral-900 min-h-dvh outline outline-1 outline-zinc-800 p-3 pt-0 flex flex-col"
>
  <div
    class="text-neutral-400 border-b border-zinc-800 px-1 py-1 h-10 flex place-items-end"
  >
    <span class="h-fit pb-0.5 pr-2">PORTAFOLIO</span>
    {#if $isLogged}
      <div class="h-fit ml-auto flex gap-1">
        <button
          class="p-1 rounded-full hover:bg-neutral-800 hover:text-neutral-300" on:click={() => openInputNewElement("file")}
        >
          <Icon src={VscNewFile} size={20} />
        </button>
        <button
          class="p-1 rounded-full hover:bg-neutral-800 hover:text-neutral-300" on:click={() => openInputNewElement("folder")}
        >
          <Icon src={VscNewFolder} size={20} />
        </button>
      </div>
    {/if}
  </div>
  <div class="flex flex-col py-1">
    {#if creatingElement}

      <div class=" max-w-full text-neutral-400 flex flex-col">
        <div class="flex flex-row gap-1">
          <input type="text" class=" flex-grow bg-neutral-800 text-neutral-300" on:input={e => updateNameNewElement(e)}>
          <button class=" ml-auto rounded-full flex-grow p-1 hover:bg-neutral-800 hover:text-neutral-300" on:click={createNewElement}>
            <Icon src={VscCheck} size={20}/>
          </button>
          <button class=" rounded-full p-1 hover:bg-neutral-800 hover:text-neutral-300" on:click={closeInputNewElement}>
            <Icon src={VscChromeClose} size={20}/>
          </button>
        </div>
        {#if creatingType === "file"}
        <div class="flex flex-row gap-2">
          <span>Template: </span>
          <div class="flex flex-row gap-2">
            <button class="px-1 hover:text-neutral-300 hover:border-b {templateSelected === 'Blank' ? 'border-b' : ''}" on:click={e => selectTemplate(e)}>Blank</button>
            <button class="px-1 hover:text-neutral-300 hover:border-b {templateSelected === 'Project' ? 'border-b' : ''}" on:click={e => selectTemplate(e)}>Project</button>
          </div>
        </div>
        {/if}
      </div>
    {/if}
    {#if Array.isArray($mainData)}
      {#each $mainData as element}
        <ExpElement dataElement={element} />
      {/each}
    {/if}
  </div>
  <div
    class="{$loginVisible
      ? 'text-neutral-300'
      : 'text-neutral-400'} mt-auto flex flex-col place-items-center"
  >
    <button
      on:contextmenu={e=>{toggleLogin();e.preventDefault()}} on:click={toogleContact}
      class="p-2 hover:text-neutral-300 w-fit justify-self-center"
    >
      <Icon src={VscAccount} size={30} />
    </button>
    {#if $isLogged}
      <p>{$usernameSession}</p>
    {/if}
  </div>
  {#if $loginVisible}
    <div transition:slide>
      {#if $isLogged}
        <Logout />
      {:else}
        <FormLogin />
      {/if}
    </div>
  {:else if contactVisible}
    <div transition:slide class="flex flex-col gap-1 text-neutral-900 place-items-center">
      <ContactCard url="https://github.com/Axxell04" name="GitHub" icon={BsGithub}/>
      <ContactCard url="https://linkedin.com/in/axxell04" name="Linkedin" icon={BiLogoLinkedin}/>
      <button class="flex flex-row gap-1 bg-neutral-400 rounded-full py-1 px-2 hover:bg-neutral-300" on:click={toogleContactForm}>
        <Icon src={SiGmail} size={25}/>
        <span class="font-semibold">Gmail</span>
      </button>
      {#if contactFormVisible}
      <div transition:slide>
        <FormContact />
      </div>
      {/if}  
    </div>
  {/if}

</div>
