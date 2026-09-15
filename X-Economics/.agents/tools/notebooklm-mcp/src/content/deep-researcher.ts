/**
 * Deep Researcher Module — v6 (DOM-verified selectors from real dump)
 *
 * REAL DOM SELECTORS (verified May 2026):
 *
 * Textarea:
 *   selector: textarea.query-box-textarea
 *   aria-label: "Khám phá nguồn dựa trên truy vấn đã nhập"
 *   parent: mat-form-field.query-box-input
 *
 * Web dropdown:
 *   selector: button.corpus-select.corpus-menu-trigger
 *   text: "languageWebkeyboard_arrow_down"
 *
 * Mode dropdown:
 *   selector: button.corpus-select.researcher-menu-trigger
 *   text: "search_spark Nghiên cứu nhanh keyboard_arrow_down"
 *   NOTE: DISABLED when Deep Research results are showing
 *
 * Import button (after Deep Research completes):
 *   selector: button.source-discovery-completed-action-import-button
 *   text: "add Nhập"
 *
 * Source panel:
 *   selector: section.source-panel
 *   content: div.source-panel-content
 *   discovery container: div.source-discovery-container
 *   completed container: div.source-discovery-completed-container
 *
 * CRITICAL: All controls are in MAIN PAGE DOM, NOT in .cdk-overlay-pane
 * Only dropdown MENUS (mat-menu) appear in overlay when clicked.
 */

import type { Page } from 'patchright';
import { randomDelay } from '../utils/stealth-utils.js';
import { log } from '../utils/logger.js';

export interface DeepResearchInput {
  query: string;
  timeoutMs?: number;
}

export interface DeepResearchResult {
  success: boolean;
  sourcesAdded?: number;
  message?: string;
  error?: string;
  domDump?: string;
}

export class DeepResearcher {
  private page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async performDeepResearch(input: DeepResearchInput): Promise<DeepResearchResult> {
    const { query, timeoutMs = 300000 } = input;
    log.info(`🔬 [DeepResearch] Starting: "${query.substring(0, 80)}..."`);

    try {
      // GUARD: Verify browser is on the correct notebook page
      const currentUrl = this.page.url();
      log.info(`  🔍 [GUARD] Current page URL: ${currentUrl}`);
      const notebookIdMatch = currentUrl.match(
        /notebook\/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/
      );
      if (!notebookIdMatch) {
        log.error(`  ❌ NOT on a notebook page! URL: ${currentUrl}`);
        throw new Error(
          `DeepResearch aborted: NOT on a notebook page. URL: ${currentUrl}`
        );
      }
      log.info(`  ✅ Confirmed on notebook: ${notebookIdMatch[1]}`);

      // DEBUG: Take a screenshot and dump DOM
      await this.page.screenshot({ path: '/tmp/nblm_debug.png' });
      const domHtml = await this.page.content();
      const fs = await import('fs');
      fs.writeFileSync('/tmp/nblm_dom.html', domHtml);
      log.info(`  📸 DEBUG: Screenshot saved to /tmp/nblm_debug.png`);

      // Wait for page to stabilize
      await randomDelay(3000, 4000);

      // Count sources before
      const sourcesBefore = await this.countSources();
      log.info(`  📊 Sources before: ${sourcesBefore}`);

      // ═══════════════════════════════════════════════════════
      // STEP 0: ALWAYS dismiss overlays first!
      // When navigating to a notebook (especially empty ones),
      // NotebookLM shows an "Add sources" overlay dialog.
      // This overlay contains its OWN Deep Research controls
      // which are DIFFERENT from the main page controls.
      // Using the overlay controls creates a NEW notebook.
      // We MUST close this overlay to use the MAIN PAGE controls.
      // ═══════════════════════════════════════════════════════
      log.info('  🔄 Dismissing any overlay dialogs...');
      await this.dismissOverlays();
      await randomDelay(1000, 2000);

      // ═══════════════════════════════════════════════════════
      // CHECK 1: Is the Import button already visible?
      // (Deep Research may have completed from a previous run)
      // ═══════════════════════════════════════════════════════
      const importResult = await this.tryClickImport(sourcesBefore);
      let currentSourcesBefore = sourcesBefore;
      if (importResult && importResult.success) {
        log.info('  🔄 Successfully imported pending sources from previous run. Proceeding with new research query...');
        currentSourcesBefore = await this.countSources();
      }

      // ═══════════════════════════════════════════════════════
      // STEP 1: Switch to Deep Research mode (main page controls)
      // ═══════════════════════════════════════════════════════
      await this.switchToDeepResearch();

      // ═══════════════════════════════════════════════════════
      // STEP 2: Type query into textarea (main page)
      // ═══════════════════════════════════════════════════════
      await this.typeQuery(query);

      // ═══════════════════════════════════════════════════════
      // STEP 3: Submit search
      // ═══════════════════════════════════════════════════════
      await this.submitSearch();

      // ═══════════════════════════════════════════════════════
      // STEP 4: Wait for completion and click Import
      // ═══════════════════════════════════════════════════════
      return await this.waitForCompletion(timeoutMs, currentSourcesBefore);
    } catch (error) {
      const msg = error instanceof Error ? error.message : String(error);
      log.error(`❌ [DeepResearch] ${msg}`);
      return { success: false, error: msg };
    }
  }

  // ──────────────── Overlay Dismissal ────────────────

  /**
   * Dismiss any Angular Material overlay/popup that may be blocking interaction.
   *
   * CONTEXT: When a previous Deep Research completed but "Import" was not clicked,
   * reopening the notebook triggers a popup (e.g. "add source" dialog) that creates
   * a cdk-overlay-backdrop covering the Import button. This method detects and
   * dismisses such overlays using standard Angular Material mechanisms (Escape key,
   * backdrop click) before any button interaction.
   *
   * Returns true if an overlay was found and dismissed.
   */
  private async dismissOverlays(): Promise<boolean> {
    let dismissed = false;

    // CRITICAL: ALWAYS dismiss overlays. The "Add sources" overlay dialog
    // contains its OWN Deep Research controls that create a NEW notebook
    // if used. We MUST close this overlay to interact with the MAIN PAGE
    // Deep Research controls which operate on the CURRENT notebook.
    //
    // Previous bug: We kept the overlay open when it had a query-box-textarea,
    // thinking it was the Deep Research form. It was NOT — it was the overlay's
    // own copy that creates research in a new context.

    // Strategy: Try closing the overlay dialog's close button first
    try {
      const closeBtn = this.page.locator('.cdk-overlay-pane button.close-button, .cdk-overlay-pane button[aria-label="Đóng"], .cdk-overlay-pane button[aria-label="Close"]').first();
      if (await closeBtn.isVisible({ timeout: 1500 })) {
        await closeBtn.click({ force: true });
        log.success('  ✅ Overlay dismissed via close button');
        dismissed = true;
        await randomDelay(500, 800);
      }
    } catch { /* no close button */ }

    // Check for active overlay backdrops (Angular Material CDK overlay)
    const backdropSelector = '.cdk-overlay-backdrop.cdk-overlay-backdrop-showing';
    try {
      const backdrop = this.page.locator(backdropSelector).first();
      if (await backdrop.isVisible({ timeout: 1000 })) {
        log.warning('  ⚠️ Detected blocking overlay backdrop — dismissing...');

        // Strategy 1: Press Escape (standard Angular Material dialog dismissal)
        await this.page.keyboard.press('Escape');
        await randomDelay(500, 800);

        // Check if overlay was dismissed
        const stillVisible = await backdrop.isVisible({ timeout: 500 }).catch(() => false);
        if (!stillVisible) {
          log.success('  ✅ Overlay dismissed via Escape key');
          dismissed = true;
        } else {
          // Strategy 2: Click the backdrop itself
          log.info('  🔄 Escape did not dismiss overlay, trying backdrop click...');
          await backdrop.click({ force: true });
          await randomDelay(500, 800);

          const stillVisible2 = await backdrop.isVisible({ timeout: 500 }).catch(() => false);
          if (!stillVisible2) {
            log.success('  ✅ Overlay dismissed via backdrop click');
            dismissed = true;
          } else {
            // Strategy 3: Double Escape
            await this.page.keyboard.press('Escape');
            await randomDelay(500, 800);
            dismissed = true;
            log.info('  ℹ️ Sent second Escape, proceeding...');
          }
        }

        await randomDelay(300, 500);
      }
    } catch {
      // No overlay found — that's fine
    }

    return dismissed;
  }

  // ──────────────── Import Check ────────────────

  /**
   * Check if the Import button is already visible and click it.
   * Returns a result if import was successful, null otherwise.
   *
   * IMPORTANT: Calls dismissOverlays() first to handle the case where a previous
   * Deep Research completed but Import was not clicked, leaving a popup that
   * blocks the Import button.
   */
  private async tryClickImport(sourcesBefore: number): Promise<DeepResearchResult | null> {
    log.info('  🔍 Checking for existing Import button...');

    // STEP 2: Look for the Import button using the exact DOM-verified selector
    // Primary: the specific class from NotebookLM's source discovery UI
    const importBtn = this.page.locator('button.source-discovery-completed-action-import-button').first();

    try {
      if (await importBtn.isVisible({ timeout: 3000 })) {
        log.success('  ✅ Import button found! Clicking to import sources...');

        // Click the Import button
        await importBtn.click({ force: true });
        log.info('  ✅ Import button clicked');
        await randomDelay(5000, 8000); // Wait for sources to be imported

        // Check new source count
        const newCount = await this.countSources();
        const added = newCount - sourcesBefore;

        if (added > 0) {
          log.success(`  ✅ Imported ${added} new source(s)!`);
          return {
            success: true,
            sourcesAdded: added,
            message: `Imported ${added} source(s) from completed Deep Research.`,
          };
        }

        // Even if count didn't change, import was clicked — wait longer
        log.info('  ⚠️ Import clicked but source count unchanged, waiting more...');
        await randomDelay(10000, 15000);

        const finalCount = await this.countSources();
        const finalAdded = finalCount - sourcesBefore;
        if (finalAdded > 0) {
          return {
            success: true,
            sourcesAdded: finalAdded,
            message: `Imported ${finalAdded} source(s) from completed Deep Research.`,
          };
        }

        return {
          success: true,
          sourcesAdded: 0,
          message: 'Import button clicked. Sources may be processing.',
        };
      }
    } catch {
      // Import button not visible
    }

    log.info('  ℹ️ No Import button found, proceeding with new Deep Research...');
    return null;
  }

  // ──────────────── Source counting ────────────────

  private async countSources(): Promise<number> {
    try {
      // From DOM dump: checkboxes are mdc-checkbox--selected
      const c1 = await this.page.locator('.single-source-container').count();
      const c2 = await this.page.locator('input.mdc-checkbox__native-control').count();
      // Subtract 1 for "Select All" checkbox if present
      const checkboxCount = c2 > 0 ? c2 - 1 : 0;
      return Math.max(c1, checkboxCount);
    } catch {
      return 0;
    }
  }

  // ──────────────── Step 1: Switch to Deep Research ────────────────

  private async switchToDeepResearch(): Promise<void> {
    log.info('  🔄 Switching to Deep Research mode...');

    // 1. Check current mode display
    const trigger = this.page.locator('button.corpus-select.researcher-menu-trigger, button.corpus-select:has-text("Nghiên cứu nhanh"), button.corpus-select:has-text("Nghiên cứu sâu"), button.corpus-select:has-text("Deep Research"), button.corpus-select:has(mat-icon:has-text("search_spark"))').first();
    if (await trigger.isVisible({ timeout: 3000 })) {
      const text = await trigger.textContent();
      log.info(`  🔍 Current mode trigger text: "${text?.trim()}"`);
      
      if (text && (text.includes('Deep Research') || text.includes('Nghiên cứu sâu'))) {
        log.info('  ✅ Mode is already set to Deep Research.');
        return;
      }

      // 2. Click to open menu
      log.info('  🖱️ Clicking researcher-menu-trigger to open mode menu...');
      await trigger.click({ force: true });
      await randomDelay(1000, 1500);

      // 3. Click the Deep Research button in overlay
      const deepBtn = this.page.locator('.cdk-overlay-pane button.research-option-deep-research, .cdk-overlay-pane button:has-text("Deep Research"), .cdk-overlay-pane button:has-text("Nghiên cứu sâu")').first();
      if (await deepBtn.isVisible({ timeout: 2000 })) {
        log.info('  🖱️ Clicking "Deep Research" button in menu overlay...');
        await deepBtn.click({ force: true });
        await randomDelay(1500, 2500);
        
        // Verify changes
        const updatedText = await trigger.textContent();
        log.success(`  ✅ Switched to Deep Research mode. Trigger text now: "${updatedText?.trim()}"`);
        return;
      } else {
        log.warning('  ⚠️ Could not find Deep Research button in overlay pane.');
      }
    } else {
      log.warning('  ⚠️ Could not find researcher-menu-trigger on main page.');
    }

    // Fallback: If the main page trigger is not found, try the old Add Source method
    log.info('  🔄 Falling back to old Add Source method...');
    const addSourceBtn = this.page.locator('button:has-text("Thêm nguồn"), button:has-text("Add source"), button[aria-label*="Add source" i]').first();
    if (await addSourceBtn.isVisible({ timeout: 2000 })) {
      await addSourceBtn.click({ force: true });
      await randomDelay(1000, 1500);
      
      const deepOption = this.page.locator('button.research-option-deep-research, button:has-text("Deep Research"), button:has-text("Nghiên cứu sâu")').first();
      if (await deepOption.isVisible({ timeout: 2000 })) {
        await deepOption.click({ force: true });
        await randomDelay(1500, 2500);
        log.success('  ✅ Switched to Deep Research via fallback method.');
        return;
      }
    }

    throw new Error('Failed to switch to Deep Research mode (both menu trigger and fallback failed).');
  }

  // ──────────────── Step 2: Type query ────────────────

  private async typeQuery(query: string): Promise<void> {
    log.info('  ⌨️ Typing research query into panel...');

    // Selectors for the Deep Research input box inside the panel
    const inputSelectors = [
      '[role="dialog"] textarea',
      '.cdk-overlay-pane textarea',
      '.mat-mdc-dialog-container textarea',
      'textarea[placeholder*="Research"]',
      'textarea[placeholder*="nghiên cứu" i]',
      'textarea[placeholder*="nhanh"]',
      'input[placeholder*="Research"]',
      'input[placeholder*="nghiên cứu" i]',
      'textarea:not(.query-box-textarea)' // Anything but the main chat box
    ];

    let textarea: any = null;
    for (const selector of inputSelectors) {
      try {
        const el = this.page.locator(selector).first();
        if (await el.isVisible({ timeout: 1000 })) {
          textarea = el;
          log.info(`  ✅ Found textarea: ${selector}`);
          break;
        }
      } catch {
        continue;
      }
    }

    if (!textarea) {
      throw new Error('Could not find Deep Research textarea in panel');
    }

    try {
      // Check if disabled
      const isDisabled = await textarea.isDisabled();
      if (isDisabled) {
        log.info('  ⚠️ Textarea is disabled, skipping type step');
        return;
      }

      await textarea.click({ force: true });
      await textarea.fill('');
      await randomDelay(200, 400);

      // Type using fill
      await textarea.fill(query);
      await randomDelay(300, 500);

      // Also trigger input event
      await textarea.evaluate((el: any, q: string) => {
        el.value = q;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
      }, query);

      await randomDelay(300, 500);
      const value = await textarea.inputValue();
      log.success(`  ✅ Query typed (${value.length} chars)`);
      return;
    } catch (e) {
      throw new Error(`Failed to type into textarea: ${e}`);
    }
  }

  // ──────────────── Step 3: Submit search ────────────────

  private async submitSearch(): Promise<void> {
    log.info('  📤 Submitting search...');
    await randomDelay(500, 800);

    // Try pressing Enter in the focused textarea first (often more reliable)
    try {
      // @ts-ignore
      const activeElement = await this.page.evaluate(() => document.activeElement?.tagName);
      if (activeElement === 'TEXTAREA' || activeElement === 'INPUT') {
         log.info('  ✅ Pressing Enter in active input element');
         await this.page.keyboard.press('Enter');
         await randomDelay(1500, 2000);
         return;
      }
    } catch { /* continue */ }

    // Try to find the submit button inside the panel
    const submitSelectors = [
      '[role="dialog"] button.actions-enter-button',
      '.cdk-overlay-pane button.actions-enter-button',
      '[role="dialog"] button:has-text("Nghiên cứu")',
      '[role="dialog"] button:has-text("Research")',
      '[role="dialog"] button[aria-label*="Submit" i]',
      '[role="dialog"] button[aria-label*="Gửi" i]',
      'button:has-text("Nghiên cứu nhanh")',
      'button:has-text("Deep Research")'
    ];

    for (const sel of submitSelectors) {
      try {
        const btn = this.page.locator(sel).first();
        if (await btn.isVisible({ timeout: 1000 })) {
          const isDisabled = await btn.isDisabled();
          if (!isDisabled) {
            await btn.click({ force: true });
            log.info(`  ✅ Clicked submit button: ${sel}`);
            await randomDelay(1500, 2000);
            return;
          } else {
            log.info(`  ⚠️ Submit button ${sel} is disabled`);
          }
        }
      } catch { continue; }
    }

    log.warning('  ⚠️ Could not submit search explicitly, hoping Enter worked');
  }

  // ──────────────── Step 4: Wait for completion ────────────────

  private async waitForCompletion(
    timeoutMs: number,
    sourcesBefore: number
  ): Promise<DeepResearchResult> {
    log.info(`  ⏳ Waiting for completion (timeout: ${timeoutMs / 1000}s)...`);

    const startTime = Date.now();
    const pollMs = 5000;
    let lastLog = '';
    let importClicked = false;

    while (Date.now() - startTime < timeoutMs) {
      const elapsed = Math.round((Date.now() - startTime) / 1000);

      // GUARD: still on notebook?
      const currentUrl = this.page.url();
      if (!/notebook\/[a-f0-9-]{36}/.test(currentUrl)) {
        return {
          success: false,
          error: `Browser navigated away! URL: ${currentUrl}`,
        };
      }

      // Check for Import button (exact DOM-verified selector)
      if (!importClicked) {
        const importBtn = this.page.locator(
          'button.source-discovery-completed-action-import-button'
        ).first();

        try {
          if (await importBtn.isVisible({ timeout: 1000 })) {
            log.success('  ✅ Import button appeared! Clicking...');

            // Click the Import button directly (overlays already dismissed)
            await importBtn.click({ force: true });
            importClicked = true;
            log.success('  ✅ Import button clicked!');
            await randomDelay(5000, 8000);
          }
        } catch { /* not yet */ }
      }

      // Check for new sources
      const currentSources = await this.countSources();
      const newSources = currentSources - sourcesBefore;

      if (newSources > 0) {
        log.success(`  ✅ Complete! ${newSources} new source(s) in ${elapsed}s`);
        return {
          success: true,
          sourcesAdded: newSources,
          message: `Deep Research complete. ${newSources} source(s) added in ${elapsed}s.`,
        };
      }

      // Check for progress indicators
      const inProgress = await this.hasProgressIndicator();

      const status = importClicked
        ? `Importing sources (${elapsed}s)`
        : inProgress
          ? `Researching (${elapsed}s)`
          : `Waiting for Deep Research (${elapsed}s)`;

      if (status !== lastLog) {
        log.info(`  ⏳ ${status}`);
        lastLog = status;
      }

      // Check for errors
      const err = await this.checkError();
      if (err) return { success: false, error: `Research error: ${err}` };

      await this.page.waitForTimeout(pollMs);
    }

    // Final check
    const finalSources = await this.countSources();
    const newSources = finalSources - sourcesBefore;
    if (newSources > 0) {
      return {
        success: true,
        sourcesAdded: newSources,
        message: `${newSources} source(s) added after ${timeoutMs / 1000}s.`,
      };
    }

    return {
      success: false,
      error: `Timed out after ${timeoutMs / 1000}s. Import clicked: ${importClicked}`,
    };
  }

  private async hasProgressIndicator(): Promise<boolean> {
    for (const sel of ['mat-progress-bar', '[role="progressbar"]', 'mat-progress-spinner', '[class*="spinner"]']) {
      try {
        if (await this.page.locator(sel).first().isVisible({ timeout: 500 })) return true;
      } catch { continue; }
    }
    return false;
  }

  private async checkError(): Promise<string | null> {
    try {
      const el = this.page.locator('[role="alert"], .error-message').first();
      if (await el.isVisible({ timeout: 500 })) {
        const text = await el.textContent();
        if (text && text.length > 5) return text.trim();
      }
    } catch { /* ignore */ }
    return null;
  }
}
