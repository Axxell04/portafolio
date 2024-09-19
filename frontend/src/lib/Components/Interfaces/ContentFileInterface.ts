export interface ContentBlankInterface {
    "": string
}

export interface ContentProjectInterface {
    name: string
    description: string
    technologys: string[]
    images: string[]
    url: string
    github: string
}

export function isContentBlankInterface(obj: any): obj is ContentBlankInterface {
    return (typeof obj === "object" && obj != null) && 
        (typeof obj[""] === "string")
}

export function isContentProjectInterface(obj: any): obj is ContentProjectInterface {
    return (typeof obj === "object" && obj != null) && 
        (typeof obj.name === "string" && typeof obj.description === "string" && Array.isArray(obj.technologys) && Array.isArray(obj.images) && typeof obj.url === "string")
}