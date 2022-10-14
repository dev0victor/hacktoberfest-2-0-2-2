// this script recreate cowsay linux script with nodejs
function main() {
  const args = process.argv.slice(2);
  const text = args.join(" ") || "I'm a cow";

  console.log(`
  ${"-".repeat(text.length + 4)}
  < ${text} >
  ${"-".repeat(text.length + 4)}
    \\   ^__^
      \\  (oo)\\_______
        (__)\\       )\\/\\
            ||----w | 
            ||     ||`);

}

main()