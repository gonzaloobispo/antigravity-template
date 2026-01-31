import os
import sys

def create_skill_structure(skill_name):
    base_path = f'.agent/skills/{skill_name}'
    os.makedirs(f'{base_path}/scripts', exist_ok=True)
    os.makedirs(f'{base_path}/resources', exist_ok=True)
    
    skill_md_content = f'''name: {skill_name}
description: [TODO: Add description based on the external tool]
instructions:
  - [TODO: Paste instructions from external source]
'''
    
    with open(f'{base_path}/SKILL.md', 'w') as f:
        f.write(skill_md_content)
    
    print(f'✅ Skill scaffolding created at: {base_path}')
    print('👉 NEXT STEP: Copy the external code/rules into this folder.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python install_skill.py <skill_name>')
    else:
        create_skill_structure(sys.argv[1])
