# Mermaid and Code Block Validator
$targetDir = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
$files = Get-ChildItem -Path $targetDir -Filter "*.md" | Sort-Object Name

Write-Host "================================================================"
Write-Host "VALIDATING CODE BLOCKS AND MERMAID DIAGRAMS"
Write-Host "================================================================"

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8
    
    # Count fenced code blocks
    $codeBlockStarts = [regex]::Matches($content, '```[a-zA-Z0-9_\-]*\r?\n')
    $codeBlockEnds = [regex]::Matches($content, '\r?\n```(?:\r?\n|$)')
    
    # Count mermaid blocks specifically
    $mermaidBlocks = [regex]::Matches($content, '```mermaid([\s\S]*?)```')
    
    # Check balance
    $backtickCount = ([regex]::Matches($content, '```')).Count
    $isBalanced = ($backtickCount % 2 -eq 0)
    
    Write-Host "File: $($f.Name)"
    Write-Host "  Size: $($content.Length) chars"
    Write-Host "  Code fences count: $backtickCount (Balanced: $isBalanced)"
    Write-Host "  Mermaid diagrams count: $($mermaidBlocks.Count)"
    
    # Validate each mermaid diagram for common syntax keywords
    $mIndex = 1
    foreach ($m in $mermaidBlocks) {
        $mContent = $m.Groups[1].Value.Trim()
        $firstLine = ($mContent -split '\r?\n')[0].Trim()
        $validTypes = @('flowchart', 'graph', 'sequenceDiagram', 'erDiagram', 'classDiagram', 'stateDiagram', 'gantt', 'pie', 'journey')
        $typeMatch = $validTypes | Where-Object { $firstLine.StartsWith($_) }
        if (-not $typeMatch) {
            Write-Host "    [WARNING] Mermaid #$mIndex first line: '$firstLine'"
        } else {
            # Write-Host "    Mermaid #$mIndex: $firstLine (Valid syntax type)"
        }
        $mIndex++
    }
}
