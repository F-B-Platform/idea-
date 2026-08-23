# Empirical Audit Script for Milestone M5
$targetDir = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
$files = Get-ChildItem -Path $targetDir -Filter "*.md" | Sort-Object Name

Write-Host "================================================================"
Write-Host "TEST 1: SCANNING FOR FORBIDDEN PLACEHOLDERS (TODO, TBD, FIXME, /* rest of code */, ...)"
Write-Host "================================================================"

$placeholderHits = @()
$ellipsisHits = @()

foreach ($f in $files) {
    $lines = Get-Content -Path $f.FullName -Encoding UTF8
    $lineNum = 0
    foreach ($line in $lines) {
        $lineNum++
        if ($line -match '\b(TODO|TBD|FIXME)\b' -or $line -match '/\*\s*rest of code\s*\*/' -or $line -match '//\s*rest of code' -or $line -match '//\s*tương tự' -or $line -match '//\s*giữ nguyên') {
            $placeholderHits += [PSCustomObject]@{
                File = $f.Name
                Line = $lineNum
                Content = $line.Trim()
            }
        }
        if ($line -match '^\s*\.\.\.\s*$' -or $line -match '//\s*\.\.\.' -or $line -match '/\*\s*\.\.\.\s*\*/') {
            $ellipsisHits += [PSCustomObject]@{
                File = $f.Name
                Line = $lineNum
                Content = $line.Trim()
            }
        }
    }
}

Write-Host "Found $($placeholderHits.Count) forbidden placeholder hits:"
$placeholderHits | ForEach-Object { Write-Host "  [$($_.File):$($_.Line)] $($_.Content)" }

Write-Host "`nFound $($ellipsisHits.Count) truncation ellipsis hits:"
$ellipsisHits | ForEach-Object { Write-Host "  [$($_.File):$($_.Line)] $($_.Content)" }

Write-Host "`n================================================================"
Write-Host "TEST 2: SCANNING FOR PROHIBITED LEGACY KEYWORDS"
Write-Host "Keywords: Flutter, React Native, GPS, 30s, C-23, C-24"
Write-Host "================================================================"

$legacyPatterns = @('Flutter', 'React Native', '\bGPS\b', '\b30s\b', '\bC-23\b', '\bC-24\b')
$legacyHits = @()

foreach ($f in $files) {
    $lines = Get-Content -Path $f.FullName -Encoding UTF8
    $lineNum = 0
    foreach ($line in $lines) {
        $lineNum++
        foreach ($p in $legacyPatterns) {
            if ($line -match $p) {
                $legacyHits += [PSCustomObject]@{
                    File = $f.Name
                    Line = $lineNum
                    Pattern = $p
                    Content = $line.Trim()
                }
            }
        }
    }
}

Write-Host "Found $($legacyHits.Count) legacy keyword occurrences (verifying if they are strictly deprecation/anti-pattern context):"
$legacyHits | ForEach-Object { Write-Host "  [$($_.File):$($_.Line)] [Matched: $($_.Pattern)] $($_.Content)" }

Write-Host "`n================================================================"
Write-Host "TEST 3: 62 FEATURES EMPIRICAL MATRIX & COVERAGE AUDIT"
Write-Host "C-01 to C-20 (20), S-01 to S-13 (13), M-01 to M-12 (12), A-01 to A-17 (17)"
Write-Host "================================================================"

$allFeatures = @()
1..20 | ForEach-Object { $allFeatures += ('C-{0:D2}' -f $_) }
1..13 | ForEach-Object { $allFeatures += ('S-{0:D2}' -f $_) }
1..12 | ForEach-Object { $allFeatures += ('M-{0:D2}' -f $_) }
1..17 | ForEach-Object { $allFeatures += ('A-{0:D2}' -f $_) }

Write-Host "Total expected features: $($allFeatures.Count)"

$featureReport = @()
foreach ($feat in $allFeatures) {
    $foundFiles = @()
    foreach ($f in $files) {
        $content = Get-Content -Path $f.FullName -Raw -Encoding UTF8
        if ($content -match "\b$feat\b") {
            $foundFiles += $f.Name
        }
    }
    $featureReport += [PSCustomObject]@{
        Feature = $feat
        Count = $foundFiles.Count
        Files = ($foundFiles -join ", ")
    }
}

$missingFeatures = $featureReport | Where-Object { $_.Count -eq 0 }
Write-Host "Missing features across all files: $($missingFeatures.Count)"
if ($missingFeatures.Count -gt 0) {
    $missingFeatures | ForEach-Object { Write-Host "  MISSING: $($_.Feature)" }
} else {
    Write-Host "All 62 features are present in the documentation set!"
}

Write-Host "`n--- Coverage Summary by File ---"
foreach ($f in $files) {
    $content = Get-Content -Path $f.FullName -Raw -Encoding UTF8
    $featsInFile = $allFeatures | Where-Object { $content -match "\b$_\b" }
    Write-Host "$($f.Name): $($featsInFile.Count) / 62 features mentioned"
}

Write-Host "`n================================================================"
Write-Host "TEST 4: STRUCTURAL ENTITY AUDIT"
Write-Host "1. 25 Tables in 02_Thiet_Ke_Database.md"
Write-Host "2. 10 API Groups in 03_Thiet_Ke_API_Contract.md"
Write-Host "3. 5 Route Groups in 04_ and 06_"
Write-Host "4. 5 Docker Containers in 08_Trien_Khai_He_Thong.md"
Write-Host "================================================================"

# Check 02_ Database Tables
$dbFile = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"
$dbContent = Get-Content -Path $dbFile -Encoding UTF8
$tableHeaders = $dbContent | Where-Object { $_ -match '^###\s+\d+\.\s+Bảng\s+`?([a-zA-Z0-9_]+)`?' -or $_ -match 'CREATE TABLE (IF NOT EXISTS\s+)?([a-zA-Z0-9_]+)' }
Write-Host "`n--- Database Tables in 02_Thiet_Ke_Database.md ---"
$tableHeaders | ForEach-Object { Write-Host "  $_" }

# Check 03_ API Groups
$apiFile = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md"
$apiContent = Get-Content -Path $apiFile -Encoding UTF8
$apiGroups = $apiContent | Where-Object { $_ -match '^###\s+\d+\.\s+Nhóm' -or $_ -match '^##\s+3\.\s+Chi Tiết 10 Nhóm Endpoint' -or $_ -match '^###\s+3\.\d+' }
Write-Host "`n--- API Groups in 03_Thiet_Ke_API_Contract.md ---"
$apiGroups | ForEach-Object { Write-Host "  $_" }

# Check 04_ and 06_ Route Groups
$uiFile = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md"
$uiContent = Get-Content -Path $uiFile -Encoding UTF8
$uiRouteGroups = $uiContent | Where-Object { $_ -match '\((customer|kds|staff|manager|admin)\)' }
Write-Host "`n--- Route Groups in 04_Thiet_Ke_UI_UX.md --- (Sample matches: $($uiRouteGroups.Count))"

$feFile = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md"
$feContent = Get-Content -Path $feFile -Encoding UTF8
$feRouteGroups = $feContent | Where-Object { $_ -match '\((customer|kds|staff|manager|admin)\)' }
Write-Host "`n--- Route Groups in 06_Quy_Trinh_Frontend.md --- (Sample matches: $($feRouteGroups.Count))"

# Check 08_ Docker Containers
$dockerFile = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md"
$dockerContent = Get-Content -Path $dockerFile -Encoding UTF8
$dockerServices = $dockerContent | Where-Object { $_ -match '^\s{2}[a-zA-Z0-9_\-]+:\s*$' -or $_ -match 'container_name:\s*([a-zA-Z0-9_\-]+)' -or $_ -match '^###\s+.*\bContainer\b' }
Write-Host "`n--- Docker Containers / Services in 08_Trien_Khai_He_Thong.md ---"
$dockerServices | ForEach-Object { Write-Host "  $_" }

Write-Host "`n================================================================"
Write-Host "AUDIT SCRIPT COMPLETED"
Write-Host "================================================================"
