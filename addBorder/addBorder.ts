function addBorder(picture: string[]): string[] {
    const lenChar = picture[1].length
    
    let topBottomBorder = '*'.repeat(lenChar + 2);
    
    const content = picture.map(el => {return `*${el}*`})
    
    picture.map((el,idx )=> { picture[idx] = `*${el}*`});
    picture.unshift(topBottomBorder)
    picture.push(topBottomBorder)
    return picture
}

console.log(addBorder(["abc", "ded", "cdc"]));