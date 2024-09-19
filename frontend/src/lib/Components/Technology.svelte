<script lang="ts">
  import { Icon } from "svelte-icons-pack";
  import type { IconType } from "svelte-icons-pack";
  import { BiHelpCircle } from "svelte-icons-pack/bi";

  import { IoLogoPython } from "svelte-icons-pack/io";
  import {
    SiFastapi,
    SiFirebase,
    SiFlask,
    SiFlutter,
    SiGo,
    SiJavascript,
    SiKotlin,
    SiNextdotjs,
    SiNodedotjs,
    SiNumpy,
    SiOpenai,
    SiPostgresql,
    SiQt,
    SiRedis,
    SiRust,
    SiSpring,
    SiSpringboot,
    SiSqlalchemy,
    SiSqlite,
    SiSvelte,
    SiTensorflow,
    SiDjango,
    SiHtml5,
    SiCss3,
    SiTailwindcss,
    SiReact,
    SiCplusplus,
    SiExpo, SiMysql,
    SiTypescript

  } from "svelte-icons-pack/si";
  import { FaBrandsJava } from "svelte-icons-pack/fa";

  export let name: string;

  const icons: { [key: string]: IconType } = {
    python: IoLogoPython,
    javascript: SiJavascript,
    django: SiDjango,
    html: SiHtml5,
    css: SiCss3,
    tailwind: SiTailwindcss,
    react: SiReact,
    reactnative: SiReact,
    "c++": SiCplusplus,
    expo: SiExpo,
    fastapi: SiFastapi,
    firebase: SiFirebase,
    flask: SiFlask,
    flutter: SiFlutter,
    go: SiGo,
    kotlin: SiKotlin,
    next: SiNextdotjs,
    nodejs: SiNodedotjs,
    numpy: SiNumpy,
    openai: SiOpenai,
    postgresql: SiPostgresql,
    qt: SiQt,
    redis: SiRedis,
    rust: SiRust,
    spring: SiSpring,
    springboot: SiSpringboot,
    sqlalchemy: SiSqlalchemy,
    sqlite: SiSqlite,
    svelte: SiSvelte,
    tensorflow: SiTensorflow,
    java: FaBrandsJava,
    mysql: SiMysql,
    typescript: SiTypescript
  };

  const getIcon: (name: string) => IconType = (name) => {
    return icons[name] || BiHelpCircle;
  };
</script>

<div class="flex flex-col place-items-center">
  <Icon src={getIcon(name.toLowerCase())} size={40} />
  <span class="text-xl">{name}</span>
</div>
