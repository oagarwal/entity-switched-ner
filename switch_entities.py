from sys import argv

def read_lines(filename):
    lines = []
    with open(entity_file, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def write_new_entity(new_ent, tag, f):
    for e in new_ent.split():
        f.write(e + " " + tag + "\n")

def switch_entities(input_file, output_file, entities):
    prev_tag = "O"
    ent = ""
    ent_id = 0

    with open(input_file, "r") as fr, open(output_file, "w") as fw:
        for line in fr:
            line = line.strip()
            if line:
                if 'DOCSTART' in line:
                    fw.write(line + "\n")
                    continue
                line  = line.split()
                word = line[0]
                tag = line[-1]
                if tag != prev_tag and ent:
                    new_ent = entities[ent_id]
                    write_new_entity(new_ent, prev_tag, fw)
                    ent_id += 1
                    ent = ""
                if tag != "O":
                    if tag != prev_tag:
                        ent = word
                    else:
                        ent += " " + word
                else:
                    fw.write(" ".join(line) + "\n")
                prev_tag = tag
            else:
                if ent:
                    new_ent = entities[ent_id]
                    write_new_entity(new_ent, tag, fw)
                    ent_id += 1
                    prev_tag = "O"
                    ent = ""
                fw.write("\n")

if __name__ == "__main__":
    input_file = argv[1]
    entity_file = argv[2]
    output_file = argv[3]
    entities = read_lines(entity_file)
    switch_entities(input_file, output_file, entities)
