# Detailed Entity Deep-Dive Script
$ErrorActionPreference = "Stop"

Write-Host "================================================================"
Write-Host "DEEP-DIVE 1: 25 DATABASE TABLES IN 02_Thiet_Ke_Database.md"
Write-Host "================================================================"
$dbContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md" -Raw -Encoding UTF8
$tables = [regex]::Matches($dbContent, 'CREATE TABLE\s+(?:IF NOT EXISTS\s+)?([a-zA-Z0-9_]+)\s*\(') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique

Write-Host "Extracted Table Count: $($tables.Count)"
$i = 1
foreach ($tbl in $tables) {
    Write-Host ("  {0:D2}. {1}" -f $i, $tbl)
    $i++
}

# Check key columns mentioned in requirements:
# Orders: delivery_address, delivery_fee, order_type
# BranchWifiConfigs: BSSID, IP Subnet
# LoyaltyCupTransactions: 10 ly tang 1
# ProductBOMs / recipes_bom: BOM
# Ingredients: ingredients
# Shifts / CashShifts / Attendances
Write-Host "`n--- Verifying Key Columns in Database Schema ---"
$keyChecks = @(
    @{ Table = "orders"; Column = "delivery_address" },
    @{ Table = "orders"; Column = "delivery_fee" },
    @{ Table = "orders"; Column = "order_type" },
    @{ Table = "branch_wifi_configs"; Column = "bssid" },
    @{ Table = "branch_wifi_configs"; Column = "subnet_mask" },
    @{ Table = "loyalty_cup_transactions"; Column = "cups_accumulated" },
    @{ Table = "recipes_bom"; Column = "ingredient_id" },
    @{ Table = "ingredients"; Column = "current_stock" },
    @{ Table = "shifts"; Column = "initial_cash" },
    @{ Table = "attendances"; Column = "bssid" }
)

foreach ($kc in $keyChecks) {
    $present = $dbContent -match "$($kc.Column)"
    Write-Host "  Checking column [$($kc.Table).$($kc.Column)]: $(if ($present) {'FOUND (PASS)'} else {'NOT FOUND (FAIL)'})"
}

Write-Host "`n================================================================"
Write-Host "DEEP-DIVE 2: 10 API GROUPS IN 03_Thiet_Ke_API_Contract.md"
Write-Host "================================================================"
$apiContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md" -Encoding UTF8
$apiGroupLines = $apiContent | Where-Object { $_ -match '^###\s+3\.\d+\s+Nhóm\s+Endpoint\s+\d+:' -or $_ -match '^###\s+2\.\d+\s+Nhóm\s+Endpoint\s+\d+:' -or $_ -match '^##\s+2\.\s+Chi Tiết 10 Nhóm Endpoint' -or $_ -match 'Nhóm Endpoint \d+:' }
Write-Host "Extracted API Groups:"
$apiGroupLines | ForEach-Object { Write-Host "  $_" }

Write-Host "`n================================================================"
Write-Host "DEEP-DIVE 3: 5 ROUTE GROUPS IN 04_ AND 06_"
Write-Host "================================================================"
$uiContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md" -Raw -Encoding UTF8
$feContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md" -Raw -Encoding UTF8

$expectedRoutes = @('(customer)', '(kds)', '(staff)', '(manager)', '(admin)')
Write-Host "Checking 04_Thiet_Ke_UI_UX.md:"
foreach ($r in $expectedRoutes) {
    $matchCount = ([regex]::Matches($uiContent, [regex]::Escape($r))).Count
    Write-Host "  Route Group $r : $matchCount occurrences"
}

Write-Host "`nChecking 06_Quy_Trinh_Frontend.md:"
foreach ($r in $expectedRoutes) {
    $matchCount = ([regex]::Matches($feContent, [regex]::Escape($r))).Count
    Write-Host "  Route Group $r : $matchCount occurrences"
}

Write-Host "`n================================================================"
Write-Host "DEEP-DIVE 4: 5 DOCKER CONTAINERS IN 08_Trien_Khai_He_Thong.md"
Write-Host "================================================================"
$devopsContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md" -Raw -Encoding UTF8
$containerMatches = [regex]::Matches($devopsContent, 'container_name:\s*([a-zA-Z0-9_\-]+)') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique

Write-Host "Extracted Container Names count: $($containerMatches.Count)"
$containerMatches | ForEach-Object { Write-Host "  Container: $_" }

Write-Host "`n================================================================"
Write-Host "DEEP-DIVE 5: FULL FEATURE MATRIX AUDIT ACROSS ALL ACTORS"
Write-Host "================================================================"

$actorSpecs = @(
    @{ Name = "Customer"; Prefix = "C"; Start = 1; End = 20; Total = 20 },
    @{ Name = "Staff"; Prefix = "S"; Start = 1; End = 13; Total = 13 },
    @{ Name = "Manager"; Prefix = "M"; Start = 1; End = 12; Total = 12 },
    @{ Name = "Admin"; Prefix = "A"; Start = 1; End = 17; Total = 17 }
)

$reqContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md" -Raw -Encoding UTF8
$testContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md" -Raw -Encoding UTF8
$readmeContent = Get-Content "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\README.md" -Raw -Encoding UTF8

foreach ($actor in $actorSpecs) {
    Write-Host "`n--- Actor: $($actor.Name) ($($actor.Total) features: $($actor.Prefix)-01 ~ $($actor.Prefix)-$($actor.End)) ---"
    for ($num = $actor.Start; $num -le $actor.End; $num++) {
        $fCode = ('{0}-{1:D2}' -f $actor.Prefix, $num)
        
        $in01 = $reqContent -match "\b$fCode\b"
        $in03 = $apiContent -match "\b$fCode\b"
        $in04 = $uiContent -match "\b$fCode\b"
        $in07 = $testContent -match "\b$fCode\b"
        $inReadme = $readmeContent -match "\b$fCode\b"
        
        $status = if ($in01 -and $in03 -and $in04 -and $in07 -and $inReadme) { "PASS (5/5 core docs)" } else { "CHECK ($in01,$in03,$in04,$in07,$inReadme)" }
        Write-Host "  $fCode : $status"
    }
}
