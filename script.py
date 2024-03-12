import sys

def bump_cmake_project_version():
    if len(sys.argv) < 3:
        print("insufficient arguments provided")
        return
    
    file_path = sys.argv[1]
    # TODO: check if file exist

    bump_types = [ "major", "minor", "patch"]
    selected_bump_type = sys.argv[2]
    selected_bump_position = bump_types.index(selected_bump_type)
    if selected_bump_type not in bump_types:
        print("available bump types: major, minor, patch")
        return

    f = open(file_path, "r")
    content = f.read()
    f.close()

    # parse
    project_position_start = content.find("project(")
    project_position_end = content.find(")", project_position_start)

    version_position = content.find("VERSION", project_position_start, project_position_end)

    versions = content[version_position + 8 : project_position_end].split(".")

    # bump correct version
    versions[selected_bump_position] = str(int(versions[selected_bump_position]) + 1)
    # reset previous versions
    for i in range(selected_bump_position + 1, 3):
        versions[i] = "0"

    print(versions)

    # compose out
    out: str = content[:version_position] + "VERSION " + ".".join(versions) + content[project_position_end:]

    # write out
    f = open(file_path, "w")
    f.truncate(0)
    f.write(out)
    f.close()

bump_cmake_project_version()